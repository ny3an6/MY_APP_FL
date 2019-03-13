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
            let table = document.getElementById("dynamic");
            let row = table.insertRow(table.rows.length);

            let cell1 = row.insertCell(0);
            let cell2 = row.insertCell(1);
            let cell3 = row.insertCell(2);
            let cell4 = row.insertCell(3);
            cell1.innerHTML = data.id;
            cell2.innerHTML = data.name;
            cell3.innerHTML = data.author;
            cell4.innerHTML = data.content;
            
           
            
            
            };
        
            const data = new FormData();
            data.append('name', name_1);
            data.append('author', author_1);
            data.append('content', content_1);
            console.log(data);
            
            xhr.send(data);
            
            return false;
        };

        
   });


