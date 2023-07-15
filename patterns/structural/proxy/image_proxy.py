from abc import ABC, abstractmethod


# 图像接口
class Image(ABC):
    @abstractmethod
    def display(self):
        pass


# 真实图像类
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print("正在加载图像:", self.filename)

    def display(self):
        print("显示图像:", self.filename)


# 图像代理类
class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


# 客户端代码
if __name__ == '__main__':
    # 创建图像代理
    image_proxy = ImageProxy("./image_proxy.png")

    # 第一次初始化代理回去调用真实类
    image_proxy.display()

    # 第二次调用时已经加载图像，直接显示
    image_proxy.display()
