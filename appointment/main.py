from fastapi import FastAPI


app = FastAPI()


@app.get('/appointments/{event}')
async def appointments(event):
    получить все записи
    отфоратировать полученные данные
    отправить данные пользователю
