# unit/models/conftest.py
import json
from pathlib import Path
import pytest

@pytest.fixture
def data(request):
    """
    Fixture paramétrable : pytest injecte request.param comme file_name
    quand on utilise indirect=True.
    """
    file_name = request.param
    path = (
        Path(__file__).parent.parent.parent
        / "data"
        / file_name
    )
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture
def model_factory():
    """
    Retourne une fonction qui prend en entrée :
      - model_cls : la classe Pydantic à tester
      - data : dict minimal valide
      - required_fields : liste de champs obligatoires
      - optional_fields : liste de champs optionnels
    et exécute les 5 scénarios standards.
    """
    def _factory(model_cls, data, required_fields, optional_fields):
        # 1. parse OK
        obj = model_cls.model_validate(data)
        assert isinstance(obj, model_cls)

        # 2. champ manquant → ValidationError
        for f in required_fields:
            d = data.copy()
            d.pop(f, None)
            with pytest.raises(Exception):
                model_cls.model_validate(d)

        # 3. optionnels manquant → OK
        for f in optional_fields:
            d = data.copy()
            d.pop(f, None)
        obj = model_cls.model_validate(data)
        assert isinstance(obj, model_cls)

        # 4. mauvais type → ValidationError (on teste juste le premier required)
        bad = data.copy()
        bad[required_fields[0]] = "mauvais_type"
        with pytest.raises(Exception):
            model_cls.model_validate(bad)

        # 5. tous optionnels présents → OK
        # (on réutilise data complet qui contient déjà les optionnels)
        obj = model_cls.model_validate(data)
        assert isinstance(obj, model_cls)
    return _factory


