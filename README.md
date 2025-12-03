# AutoPriceAI - ML сервис предсказания цен на автомобили

Веб-сервис для автоматической оценки стоимости автомобилей на основе машинного обучения. Сервис принимает 11 параметров автомобиля и через веб-интерфейс посредством API возвращает предсказанную цену.

## Модель и метрики

**Модель:** CatBoost Regressor - градиентный бустинг с автоматической обработкой категориальных признаков. Данный алгоритм был выбран из за большого колличества категориальных значений.

**Метрики качества:**
- **R²:** 0.904 
- **MAE:** 1 119 
- **MSE:** 3 488 776

### REST API
**Endpoint:** `POST /predict/`

**Список параметров:**
```json
{
  "seller": "private",
  "vehicleType": "sedan",
  "fuelType": "benzin",
  "brand": "bmw",
  "notRepairedDamage": "no",
  "gearbox": "automatic",
  "model": "x5",
  "powerPS": 150,
  "kilometer": 50000,
  "age": 3,
  "nrOfPictures": 0
}
```
### Выборка насчитывала около 370 000 записей
<img width="1088" height="607" alt="image" src="https://github.com/user-attachments/assets/7b27477b-0d2d-4867-91d2-33f7642fd044" />

### Установка

```bash
# 1. Клонировать репозиторий
git clone https://github.com/ваш-username/car-price-prediction.git
cd car-price-prediction

# 2. Создать виртуальное окружение
python -m venv venv

# 3. Активировать окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Установить зависимости
pip install -r requirements.txt

# 5. Применить миграции
python manage.py migrate

# 6. Запустить сервер
python manage.py runserver
```


Ссылка на создание модели - https://colab.research.google.com/drive/167uVOHY655_uJf95GJvxALfhKyCY7Tns?usp=sharing
Ссылка на сервер - https://car-price-prediction-sevensemm.onrender.com/
