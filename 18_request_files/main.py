from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.post("/file/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


# UploadFileはでーたをメモリとディスクに保存する。そのため大容量ファイルでも動作する。
# さらに、メタデータの取得もできる。
@app.post("/uploadfile/")
async def create_uplaod_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.post("/files/")
async def create_files(files: list[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
