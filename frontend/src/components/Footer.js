import React from 'react';

const Footer = () => {

    return(

      <footer class="pt-4 my-md-5 pt-md-5 border-top">
        <div class="container">
        <div class="row">
          <div class=" col-md">
            <h5>Сообщество</h5>
            <ul class="list-unstyled text-small">
              <li><a class="text-muted" href="#">Выйти на связь</a></li>
              <li><a class="text-muted" href="#">Что в планах</a></li>
              <li><a class="text-muted" href="#">Задонатить на кофе</a></li>
            </ul>
          </div>
          <div class=" col-md">
            <h5>Ресурсы</h5>
            <ul class="list-unstyled text-small">
              <li><a class="text-muted" href="https://gb.ru">Geekbrains</a></li>
              <li><a class="text-muted" href="https://t.me/the-nans">Telegram</a></li>
              <li><a class="text-muted" href="#">Github</a></li>
            </ul>
          </div>
          <div class=" col-md">
            <h5>Про нас</h5>
            <ul class="list-unstyled text-small">
              <li><a class="text-muted" href="#">Команда</a></li>
              <li><a class="text-muted" href="#">Безопасность</a></li>
              <li><a class="text-muted" href="#">Соглашение</a></li>
            </ul>
          </div>
        </div>
        </div>
      </footer>
    )
}

export default Footer