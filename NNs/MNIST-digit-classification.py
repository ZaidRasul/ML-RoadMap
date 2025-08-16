from torchvision import datasets
from torchvision.transforms import ToTensor #so we can convert the images to tensors
from torch.utils.data import DataLoader

train_data = datasets.MNIST(
    root = 'data',
    train = True, # telling it to load the training dataset
    download = True, # to download the dataset 
    transform = ToTensor()
)

test_data = datasets.MNIST(
    root = 'data',
    train = False, # telling it to load the test dataset
    download = True, # to download the dataset 
    transform = ToTensor()
)
