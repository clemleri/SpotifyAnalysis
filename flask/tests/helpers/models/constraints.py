# helpers/models/constraints.py

import pytest
from pydantic import ValidationError

def assert_constr_regex_field(
    model_cls,           # la classe Pydantic, ex. SimplifiedTrack
    data: dict,          # dict complet et valide
    field: str,          # nom du champ à tester
    valid_values: list,  # liste de chaînes qui doivent passer la regex
    invalid_values: list # liste de chaînes qui doivent la violer et lever ValidationError
):
    """
    Teste qu'un champ `constr(pattern=...)` :
      - accepte toutes les valeurs de `valid_values`
      - rejette toutes celles de `invalid_values`
    """
    # Cas valides
    for good in valid_values:
        d = data.copy()
        d[field] = good
        obj = model_cls.model_validate(d)
        assert getattr(obj, field) == good, (
            f"Valeur valide '{good}' rejetée pour {model_cls.__name__}.{field}"
        )

    # Cas invalides
    for bad in invalid_values:
        d = data.copy()
        d[field] = bad
        with pytest.raises(ValidationError, match=field):
            model_cls.model_validate(d)

def assert_conint_between(
    model_cls,      # ta classe Pydantic, ex. Track
    data: dict,     # dict complet et valide
    field: str,
    min_value: int,
    max_value: int,
):
    """
    Vérifie qu'un champ integer (conint) lève pour valeur hors bornes, et passe au milieu.
    """
    # Cas valide : valeur médiane
    mid = (min_value + max_value) // 2
    d = data.copy()
    d[field] = mid
    obj = model_cls.model_validate(d)
    assert getattr(obj, field) == mid

    # Cas invalide : juste en dessous et juste au‑dessus
    for bad in (min_value - 1, max_value + 1):
        d = data.copy()
        d[field] = bad
        with pytest.raises(ValidationError):
            model_cls.model_validate(d)


def assert_non_empty_list_field(
    model_cls,
    data: dict,
    field: str,
):
    """
    Vérifie qu'une liste annotée conlist(min_length=1) lève si vide.
    """
    # Cas valide : on garde ce qui est dans data
    obj = model_cls.model_validate(data)
    assert isinstance(getattr(obj, field), list)
    assert len(getattr(obj, field)) >= 1

    # Cas invalide : liste vide
    d = data.copy()
    d[field] = []
    with pytest.raises(ValidationError):
        model_cls.model_validate(d)
        
def assert_non_empty_str_field(
    model_cls,
    data : dict,
    field : str
):
    """
    Vérifie qu'une chaine annotée constr(min_length=1) ne soit pas vide, lève si vide.
    """
    # Cas valide : on garde ce qui est dans data
    obj = model_cls.model_validate(data)
    assert len(getattr(obj, field)) >= 1

    # Cas invalide : chaine vide
    d = data.copy()
    d[field] = ""
    with pytest.raises(ValidationError):
        model_cls.model_validate(d)
        

    
def assert_conint_ge(
    model_cls,
    data : dict,
    field,
    min_value : int
):  
    """
    vérifie qu'un champ integer (conint(ge=...)) lève pour les valeurs en dessous de la borne min_value, 
    et passe pour les valeurs au dessus de la borne min_value
    """
    
    # Cas valide : valeur au supérieur ou égale à min_value
    good = min_value
    d = data.copy()
    d[field] = good
    obj = model_cls.model_validate(d)
    assert getattr(obj, field) == good
    
    # Cas invalide : valeur de field stricement inférieur de min_value
    bad = min_value-1
    d = data.copy()
    d[field] = bad
    with pytest.raises(ValidationError):
        model_cls.model_validate(d)
        

def assert_positive_int(
    model_cls,
    data : dict,
    field : str
):
    """
    vérifie qu'un champ de type integer (PositiveInt) soit bien strictement supérieur à 0
    """
    
    # Cas valide : valeur strictement supérieur à 0
    good = 1000
    d = data.copy()
    d[field] = good
    obj = model_cls.model_validate(d)
    assert getattr(obj, field) == good
    
    # Cas invalide : valeur strictement inférieur à 0
    bad = -1
    d = data.copy()
    d[field] = bad
    with pytest.raises(ValidationError):
        model_cls.model_validate(d)

def assert_literal(
    model_cls,
    data : dict,
    field : str,
    valid_values : list,
    invalid_values : list,
):
    """
    Vérifie qu'un champ str (Lietral[chaine]) accepte seulement les valeurs spécifier
    """
    
    # Cas valides
    for good in valid_values:
        d = data.copy()
        d[field] = good
        obj = model_cls.model_validate(d)
        assert getattr(obj, field) == good, (
            f"Valeur valide '{good}' rejetée pour {model_cls.__name__}.{field}"
        )
        
    # Cas invalides
    for bad in invalid_values:
        d = data.copy()
        d[field] = bad
        with pytest.raises(ValidationError, match=field):
            model_cls.model_validate(d)
            
def assert_constr_depending_literal(
    model_cls,
    data : dict,
    constr_field : str,
    literal_field : str,
    valid_values : list,
    invalid_values : list
):
    """
    Teste qu'un champ `constr(pattern=...)` dépendant d'un autre champ Literal[str]:
      - accepte toutes les valeurs de `valid_values` en fonction d'un Literal[str] donné
      - rejette toutes celles de `invalid_values` en fonction d'un Literal[str] donné
    """
    
    # Cas valide 
    for good_tuple in valid_values:
        d = data.copy()
        d[constr_field] = good_tuple[0]
        d[literal_field] = good_tuple[1]
        obj = model_cls.model_validate(d)
        assert getattr(obj, constr_field) == good_tuple[0], (
            f"Valeur valide '{good}' rejetée pour {model_cls.__name__}.{constr_field}"
        )
        assert getattr(obj, literal_field) == good_tuple[1], (
            f"Valeur valide '{good}' rejetée pour {model_cls.__name__}.{literal_field}"
        )
        
    # Cas invalide
    for bad_tuple in invalid_values:
        d = data.copy()
        d[constr_field] = bad_tuple[0]
        d[literal_field] = bad_tuple[1]
        with pytest.raises(ValidationError):
            obj = model_cls.model_validate(d)
        
    


    
    
    

    
    


        
