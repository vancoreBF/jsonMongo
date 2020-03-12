for f in *.json
do 
    echo "Procesando... $f"
    filename=$(basename "$f")
    extension="${filename##*.}"
    filename="${filename%.*}"
    mongoimport --authenticationDatabase admin -u root -p example -d mondial -c
    "$filename" --jsonArray --file "$f" --headerline
done