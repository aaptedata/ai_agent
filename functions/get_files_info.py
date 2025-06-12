import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
        # Creates an absolute path for the working directory. 
        # This ensures no matter how the user specified it, we’re working with a full path.
    target_dir = abs_working_dir
    if directory:
        # If a subdirectory is specified, we create its absolute path by joining 
        # it to the working_directory. This prevents things like accidental path escapes.
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        # Checks if the target directory is actually inside the working directory 
        # (as a security measure). If not, we return an error string.
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
        # Insures the path exists and is, indeed, a directory; 
        # if not, returns an error about it not being a directory.
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)    