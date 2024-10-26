from pydantic import BaseModel


class Dataset(BaseModel):
	id: int
	name: str
	publisher: str
	description: str
	source: str | None = None


class FullDataset(Dataset):
	data: list[dict] | None = None
