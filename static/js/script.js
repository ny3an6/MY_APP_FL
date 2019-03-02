document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#form').onsubmit = () => {
        
        const xhr = new XMLHttpRequest(); // создаст обьект который может обращаться к серверу и получить от него данные (json обьект), а также отобразить его нам     
        const name_1 = document.querySelector('#name_1').value;
        const author_1 = document.querySelector('#author_1').value;
        const content_1 = document.querySelector('#content_1').value;
        console.log(name_1);


        xhr.open('POST', '/add_book'); // настраиваем куда мы отправляем запрос 

        xhr.onload = () => { // когда мы загрузим данные которые получили с сервера выполним следующее
            const data = JSON.parse(xhr.responseText); // JSON.parse превращает текст в java script обьект(словарь)
            console.log(data)
           // data = 
           //const id = data.id;
           //const name = data.name;
           //const author = data.author;
           //const content = data.content;
           //document.querySelector('#responce_1').innerHTML = name;
           //document.querySelector('#responce_2').innerHTML = author;
           //document.querySelector('#responce_3').innerHTML = content;
           //document.querySelector('#responce_4').innerHTML = id;
            console.log(xhr.response);
            console.log(xhr.responseText);
            
            };
        
            const data = new FormData();
            data.append('name', name_1);
            data.append('author', author_1);
            data.append('content', content_1);
            console.log(data);
            
            xhr.send(data);
            alert(document.cookie)
            return false;
        };

        //document.querySelector('#form').onsubmit = () => {
        //    const xhr = new XMLHttpRequest();
        //    xhr.open('GET', '/');
        //    xhr.send();
//
     //  };
   });


