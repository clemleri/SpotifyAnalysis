from models.track import Track
from dao.track_dao import TrackDAO
import json

if __name__ == "__main__":
    ACCESS_TOKEN = "BQDAXTL_wt1ijYNTQmUNfF32AGZvcXdJCID2ci_l8bhL3XWMTbSlXp-iJH4mW3wqq9eaqOMiYZ5wJah0io5Ym7BsxSlxARapURGMosjC6AHV_aliqIYckwZGsfEQNAkEy8bVyQYiePR5mzLyi0NNXcPEaUAbia1ZxoubBDl8HEeE4QJiHqgBdx4e32abEMgw2dWVXTtdqI3H9EMypvS4eus6KJr4NC8Rynskwi8KK77EZWJE0rZ9_GZmuPCMwseptDJOdA"
    trackDAO = TrackDAO()
    res = trackDAO.fetch_track(ACCESS_TOKEN,"1BksmTSEoibC7dkI7UVENd")
    print(res)