Support tar & url support 
- Slower than copy
- Security risk for url

============Tar
tar zcvf file.tar.gz file1.html file2.html file3.html index.html
docker build -t test-add.tar .
docker run --name add-tar -p 9090:80 -d test-add.tar
curl http://localhost:9090/
docker exec -it add-tar ls -l /usr/share/nginx/html/
============Fetch from Url
Two type of files can be fetched
- URL -> https://example.com/archive.zip
- Git Release -> https://github.com/demo.git#v1.0:docs