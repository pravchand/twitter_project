# Run this bash script to move files to box folder

source_dir="C:/Users/fdmol/Desktop/Energy-Lab/twitter_search/twitter_search/data/"
destination_dir="C:/Users/fdmol/Box/Global-RCT/data"

echo "Copying user data files..."

if cp -r "$source_dir"/* "$destination_dir"/; then
  echo "Files copied successfully!"
else
  echo "Failed to copy files."
fi