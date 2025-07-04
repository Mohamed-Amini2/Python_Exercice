```markdown
# Image Processing Application (Variant 1)

Приложение для обработки изображений с возможностью:

- Загрузки изображений с диска
- Захвата фото с веб-камеры
- Применения эффектов: негатив, размытие по Гауссу, рисование кругов
- Сохранения результатов

---

## 📦 Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/Mohamed-Amini2/Python_Exercice
   cd Python_Exercice
   ```

2. **Создайте и активируйте виртуальное окружение**:
   ```bash
   python3.6 -m venv venv  # Для Python 3.6
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Использование

Запуск приложения:
```bash
python main.py
```

### Возможности:

1. **Загрузка изображения**  
   - Введите `1` и укажите путь к файлу (`JPG/PNG`).  
   - Пример: `image.jpg`

2. **Снимок с камеры**  
   - Введите `2` — программа сделает фото через 3 секунды.

3. **Эффекты**:
   - **Decrease Brightness ** (`1`): Инверсия цветов.  
   - **Resize Image** (`8`): Укажите размер ядра (нечётное число).  
   - **Draw red Circle ** (`13`): Введите координаты центра (`X Y`) и радиус.  

4. **Сохранение**  
   - Введите `4`, чтобы сохранить результат в папку `saves`.

---

## 🛠 Технические детали

### Структура проекта
```bash
practice-app/
├── main.py                  # Основной код приложения
├── requirements.txt         # Зависимости
├── utils/
│   └── helpers.py           # Загрузка/сохранение изображений
├── image_processing/
│   ├── brightness.py          
│   ├── resize.py    # Размытие по Гауссу
│   └── draw.py       # Рисование кругов
```

### Зависимости
- **OpenCV** (`opencv-python==4.5.5.64`)
- **NumPy** (`numpy==1.21.5`)

---

## 📝 Пример использования

1. Запустите приложение:  
   ```bash
   python main.py
   ```

2. Выберите источник изображения:
   ```
   1. Load from file
   2. Capture from webcam
   Enter 1 or 2: 1
   Enter image path: photo.jpg
   ```

3. Примените эффекты:
   ```
   Choose an action:
   1. Resize Image 
   8. Decrease Brightness
   13. Draw Red Circle
   Enter task number (1/8/13): 13
   Enter X coordinate: 100
   Enter Y coordinate: 150
   Enter radius: 30
   ```

4. Сохраните результат:
   ```
   Enter output file path (e.g., output.jpg): edited_photo.jpg
   ```

---

## ⚠️ Устранение проблем

**Проблема**: Не отображаются окна с изображениями  
**Решение**: Установите переменную окружения:
```bash
export QT_QPA_PLATFORM=xcb  
```

**Проблема**: Камера не работает  
**Решение**:
- Проверьте наличие камеры в настройках системы.
- Убедитесь, что другие приложения не используют камеру.
