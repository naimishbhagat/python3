import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergarter Cop", "year": 1993}
# ]
# write data to file
# data = json.dumps(movies)
# Path("movies.json").write_text(data)
# read data from file
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0]["title"])
