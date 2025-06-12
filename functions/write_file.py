import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
    # If abs_file_path is "/home/user/calculator/pkg/morelorem.txt"
    # os.path.dirname() returns "/home/user/calculator/pkg"
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    # os.path.exists checks to see if the file exists, if not, os.makedirs makes the file
    # Without exist_ok=True: If the directory already exists, makedirs would raise a FileExistsError
    # With exist_ok=True: If the directory already exists, makedirs does nothing (no error)
    
    # if not file_path:
    #     abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
       
    except Exception as e:
        return f'Error writing to file "{file_path}": {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
    
# schema_write_file = types.FunctionDeclaration(
#     name="write_file",
#     description="Writes to file.",
#     parameters=types.Schema(
#         type=types.Type.OBJECT,
#         properties={
#             "directory": types.Schema(
#                 type=types.Type.STRING,
#                 description="Writes to file.",
#             ),
#         },
#     ),
# )    