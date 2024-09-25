import os

# Create the files
for i in range(1,18):
    content = f'''# Your solution to Exercise {i+1}\n'''
    with open(f"exercises/exercise_{i+1}.py", "w") as file:
        file.write(content)

    # Create git commit for each file
    os.system("git add .")
    os.system(f"git commit -m 'Create exercise_{i+1}.py'")
    os.system("git push")
