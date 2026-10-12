# from fastapi import FastAPI, HTTPException, File, UploadFile
# from fastapi.staticfiles import StaticFiles
# import os
# import shutil

# app = FastAPI()


# # Step 1: Make sure upload folder exists

# UPLOAD_DIR = "upload"

# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)


# # Step 2: Static file setup

# app.mount(
#     "/files",
#     StaticFiles(directory=UPLOAD_DIR),
#     name="files"
# )


# # Step 3: Upload file API

# @app.post("/upload")
# def upload_file(file: UploadFile = File(...)):

#     filename = file.filename

#     if not filename:
#         raise HTTPException(
#             status_code=400,
#             detail="File does not exist"
#         )

#     file_path = os.path.join(UPLOAD_DIR, filename)

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {
#         "message": "File uploaded successfully",
#         "filename": filename,
#         "file_url": f"http://127.0.0.1:8000/files/{filename}"
#     }


# # Step 4: Get file URL API

# @app.get("/files/{filename}")
# def get_file(filename: str):

#     file_path = os.path.join(UPLOAD_DIR, filename)

#     if not os.path.exists(file_path):
#         raise HTTPException(
#             status_code=404,
#             detail="File not found"
#         )

#     return {
#         "file_url": f"http://127.0.0.1:8000/files/{filename}"
#     }


# # Step 5: Test API

# @app.get("/")
# def home():

#     return {
#         "message": "File uploading API is running"
#     }

#----------------------------------------PRACTICE-------------------------------
# from fastapi import FastAPI,File,UploadFile,HTTPException
# from fastapi.staticfiles import StaticFiles
# import os 
# import shutil

# app= FastAPI()

# UPLOAD_DIR="upload"
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)


# @app.post("/files")
# def upload_file(file: UploadFile=File(...)):
#     filename= file.filename
#     if not filename:
#         raise HTTPException(
#             status_code=401,
#             detail="filename cannot exists"
#         )
#     file_path=os.path.join(UPLOAD_DIR,filename)
#     with open(file_path,"wb") as buffer:
#         shutil.copyfileobj(file.file,buffer)
#     return {
#         "message":"file uploaded successfully",
#         "filename":filename,
#         "file_url":f"http://127.0.0.1:8000/files/{filename}"
#     }

# @app.get("/files/{filename}")
# def get_file(filename:str):
#     file_path=os.path.join(UPLOAD_DIR,filename)
#     if not os.path.exists(file_path):
#         raise HTTPException(
#             status_code=401,
#             detail="file cannot exist"
#         )
#     return {
#         f"http://127.0.0.1:8000/files/{filename}"
#     }
# @app.delete("/files/{filename}")
# def delete_file(filename: str):

#     file_path = os.path.join(UPLOAD_DIR, filename)

#     if not os.path.exists(file_path):
#         raise HTTPException(
#             status_code=404,
#             detail="File not found"
#         )

#     os.remove(file_path)

#     return {
#         "message": "File deleted successfully",
#         "filename": filename
#     }

# app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

