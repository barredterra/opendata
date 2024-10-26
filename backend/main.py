import json
from csv import DictReader
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .dataset import Dataset, FullDataset

app = FastAPI()
app.mount("/assets", StaticFiles(directory="public/assets"), name="static")


@app.get("/", response_class=FileResponse)
async def main():
	return "public/index.html"


# @app.get("/{file_path:path}", response_class=FileResponse)
# async def files(file_path: str):
#     return f"public/{file_path}"


@app.get("/api/datasets/{id}/json")
async def get_dataset(id: int) -> FullDataset | None:
	index_data = read_index()

	for dataset in index_data:
		if dataset["id"] == id:
			data = (get_data_path() / dataset["path"]).read_text()
			data = list(DictReader(data.splitlines()))
			return FullDataset(
				id=dataset["id"],
				name=dataset["name"],
				publisher=dataset["publisher"],
				source=dataset["source"],
				description=dataset["description"],
				data=data,
			)

	raise HTTPException(status_code=404, detail="Dataset not found")


@app.get("/api/datasets/{id}/csv")
async def get_dataset_csv(id: int) -> FileResponse:
	index_data = read_index()

	for dataset in index_data:
		if dataset["id"] == id:
			return FileResponse(
				path=get_data_path() / dataset["path"],
				filename=dataset["path"],
				media_type="text/csv",
			)

	raise HTTPException(status_code=404, detail="Dataset not found")


@app.get("/api/datasets")
async def get_datasets() -> list[Dataset]:
	index_data = read_index()

	return [
		Dataset(
			id=dataset["id"],
			name=dataset["name"],
			publisher=dataset["publisher"],
			source=dataset["source"],
			description=dataset["description"],
		)
		for dataset in index_data
	]


def read_index():
	path = get_data_path() / "index.json"
	return json.loads(path.read_text())


def get_data_path() -> Path:
	return Path(__file__).parent.parent / "data"
