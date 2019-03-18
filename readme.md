Python version 3.7.2

run commands 
```
    python3 __main__.py *imagepath* base
    python3 __main__.py *imagepath* color
```

Реализованные паттерны:
1 - Cостояние
2 - Цепочка обязанностей -> Создание цепочки работы 
3 - Фасад  ( много классов -> единый интерфейс работы)
4 - Посетитель ( класс которому передают объект и он определяет что с ним делать)
5 - Наблюдатель ( класс который следит за другими классами и реагирует на изменения)


# Состояние

Это поведенческий паттерн проектирования, который позволяет объектам менять поведение в зависимости от своего состояния. Извне создаётся впечатление, что изменился класс объекта.

Данный паттерн был реализован в следущем файле -> ImageHelper.py
**Код**
```
class ImageHelper:

    def __openInBaseMode(self):
        self.image = Image.open(self.pathToFile).convert('RGB')
        self.mode = Primitives().PIL
    def __openInColorMode(self):
        self.image = cv2.imread(self.pathToFile)
        self.mode = Primitives().CV2
    
    def __init__(self, path, mode):
        self.pathToFile = path
        self.image = None
        self.mode = None
        if mode == 'base':
            self.__openInBaseMode()
        elif mode == 'color':
            self.__openInColorMode()
```

# Цепочка обязанностей

Цепочка обязанностей — это поведенческий паттерн проектирования, который позволяет передавать запросы последовательно по цепочке обработчиков. Каждый последующий обработчик решает, может ли он обработать запрос сам и стоит ли передавать запрос дальше по цепи.

Данный паттерн был реализован в следующем файле -> ```__main__.py```

**Код**
```
def main(self, args):
        if len(args) <= 1:
            return 0
        img = ImageHelper(args[1], args[2])  #imgFilter.ImageUserFilters(args[1], args[2])
        observer = Observer(img)
        observer.ApplyFilter(Filters.ColorizeImage)
        observer.ApplyFilter(Filters.AddSharpness)
        observer.ApplyFilter(Filters.AddSharpness)

        img.OpenImage()
        observer.ImageSave('result')
        return
```

# Фасад

Фасад — это структурный паттерн проектирования, который предоставляет простой интерфейс к сложной системе классов, библиотеке или фреймворку.

Данный паттерн реализован в следующей папке -> ImageHelper

Данная папка содержит множетсов классов которые имеют много функционала и выведены в отедьный интерфейс для использования

**Код**

```
        observer = Observer(img)
        observer.ApplyFilter(Filters.ColorizeImage)
        observer.ApplyFilter(Filters.AddSharpness)
        observer.ApplyFilter(Filters.AddSharpness)

```

# Посетитель

Посетитель — это поведенческий паттерн проектирования, который позволяет добавлять в программу новые операции, не изменяя классы объектов, над которыми эти операции могут выполняться.


**Код**

```
class Filters(Enum):
    AddSharpness = 0
    AddBlur = 0
    AddSMOOTH = 0
    ColorizeImage = 1
    
observer = Observer(img)
observer.ApplyFilter(Filters.ColorizeImage)
observer.ApplyFilter(Filters.AddSharpness)
observer.ApplyFilter(Filters.AddSharpness)

```

# Наблюдатель

Наблюдатель — это поведенческий паттерн проектирования, который создаёт механизм подписки, позволяющий одним объектам следить и реагировать на события, происходящие в других объектах.

Данный паттерн реализован в файле -> Observer.py

**Код**

```
class Observer:
    def __init__(self, objectToObserve):
        self.parrentObject = objectToObserve
        self.object = objectToObserve.image
        self.state = objectToObserve.mode
        self.Primitives = Primitives()

    def ReOpenInBaseMode(self):
        if type(self.state) is type(self.Primitives.CV2):
            self.ImageSave('intermidiate')
            self.object = Image.open('intermidiate.jpg').convert('RGB')
            self.state = self.Primitives.PIL
            os.remove('intermidiate.jpg')
        else:
            print(self.state)
            print('it is already in Base Mode')
    def ReOpenInColorMode(self):
        if type(self.state) is type(self.Primitives.PIL):
            self.ImageSave('intermidiate')
            self.object = np.copy( cv2.imread('intermidiate.jpg'))
            self.state = self.Primitives.CV2
            os.remove('intermidiate.jpg')
        else:
            print(self.state)
            print('it is already in Color Mode')
    def ImageSave(self, name):
        if type(self.state) is type(self.Primitives.PIL):
            self.object.save(name + '.jpg', 'JPEG')
            return
        elif type(self.state) is type(self.Primitives.CV2):
            cv2.imwrite(name + '.jpg',self.object)
            return
    def ApplyFilterSettings(self, filterType):
        if filterType._value_ == 1:
            print('1')
            self.ReOpenInColorMode()
        elif filterType._value_ == 0:
            print('2')

            self.ReOpenInBaseMode()
        
    def ApplyFilter(self, callMethod):
        self.ApplyFilterSettings(callMethod)
        try:
            filters = ImageUserFilters()
            filters.setupImage(self.object)
            getattr(filters, callMethod._name_)()
            self.object = filters.image
            self.parrentObject.image = filters.image
            self.parrentObject.mode = self.state

        except Exception as ex:
            print(str(ex))
            print('this method is not implemented')

```


