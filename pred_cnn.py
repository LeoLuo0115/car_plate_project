import torch
from torchvision import transforms
import PIL.Image as Image
from CNN1 import Net





def parseOutput(output):
    INDEX_PROVINCE = {"京": 0, "沪": 1, "津": 2, "渝": 3, "冀": 4, "晋": 5, "蒙": 6, "辽": 7, "吉": 8, "黑": 9, "苏": 10,
                      "浙": 11, "皖": 12, "闽": 13, "赣": 14, "鲁": 15, "豫": 16, "鄂": 17, "湘": 18, "粤": 19, "桂": 20,
                      "琼": 21, "川": 22, "贵": 23, "云": 24, "藏": 25, "陕": 26, "甘": 27, "青": 28, "宁": 29, "新": 30}

    INDEX_LETTER = {"0": 31, "1": 32, "2": 33, "3": 34, "4": 35, "5": 36, "6": 37, "7": 38, "8": 39, "9": 40, "A": 41,
                    "B": 42, "C": 43, "D": 44, "E": 45, "F": 46, "G": 47, "H": 48, "J": 49, "K": 50, "L": 51, "M": 52,
                    "N": 53, "P": 54, "Q": 55, "R": 56, "S": 57, "T": 58, "U": 59, "V": 60, "W": 61, "X": 62, "Y": 63,
                    "Z": 64}

    PLATE_CHARS_PROVINCE = ["京", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑",
                            "苏", "浙", "皖", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤",
                            "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新"]

    PLATE_CHARS_LETTER = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "J",
                          "K", "L", "M", "N", "P",
                          "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    index = 0
    maxValue = 0
    label = ""
    output = output[0]
    for i in range(31):
        if output[i] > maxValue:
            maxValue = output[i]
            index = i
    label = label + PLATE_CHARS_PROVINCE[index]
    for j in range(6):
        index = 0
        maxValue = 0
        for i in range(34):
            if output[i+j*34+34] > maxValue:
                maxValue = output[i+j*34+34]
                index = i
        label = label + PLATE_CHARS_LETTER[index]
    return label
def CNN_pridect(net, img_path):
    trans = transforms.Compose([
                                transforms.Resize((80, 240)),
                                transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    img = Image.fromarray(img_path)
    img = trans(img)
    output = net(img)
    output_label = parseOutput(output.detach().numpy())
    return output_label


# model = Net()
# model.load_state_dict(torch.load('CNN.pth', map_location='cpu'))
# model.eval()