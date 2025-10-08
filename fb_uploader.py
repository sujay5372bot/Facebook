import requests

def upload_to_facebook(video_path, title, description, page_id, access_token):
    url = f"https://graph-video.facebook.com/v21.0/{page_id}/videos"
    data = {
        "title": title,
        "description": description
    }
    files = {
        "source": open(video_path, "rb")
    }

    response = requests.post(url, data=data, files=files, params={"access_token": access_token})
    return response.json()
