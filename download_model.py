import gdown

file_url = "https://drive.google.com/uc?id=1Sxlkrz_flJiUbtmblcTW4LNbDxShrVZK"
gdown.download(file_url, "./app/torch_models/torch_model.pt")
