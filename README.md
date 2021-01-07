# Video Merger
This project is created to merge multiple videos into a single video with the help of [moviepy](https://pypi.org/project/moviepy/).

##prerequisite

```bash
pip install moviepy
pip install moviepy.editor
```

```bash
pip install firebase_admin
pip install flask
```

##How to use it

Run this project on [local host](http://127.0.0.1:5000/ ) and at address ba type localhost/url?url1:url_of_first_video&&url2:url_of_second_video.

For example [localhost/url?url1:url&&url2:url](http://127.0.0.1:5000/url?url1:https://firebasestorage.googleapis.com/v0/b/fir-tuturial-a30a1.appspot.com/o/2.mp4?alt=media&token=4fed63b4-15e7-4352-bbe3-5ce32e7906a8&&url2:https://firebasestorage.googleapis.com/v0/b/fir-tuturial-a30a1.appspot.com/o/Introduction.mp4?alt=media&token=6c6904f0-db2a-49b8-96b0-9c599e5c7496)

This will return a json object in the form of
```bash
    d = {
        "url1": url1,
        "url2": url2,
        "url3": processed video
    }
```



