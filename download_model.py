import gdown

file_url = "https://drive.google.com/uc?id=1tEBjBoQKrFe3u0X6Jd89F5YlGy-SiERz"
gdown.download(file_url, "./app/torch_models/torch_model.pt")
