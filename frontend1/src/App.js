import React from "react";
import UserList from "./components/User.js";
import Footer from "./components/Footer.js";
import Menu from "./components/Menu.js";
import axios from "axios";
class App extends React.Component{

        constructor(props){
            super(props);
            this.state = {
                'users': []
            }

        }

componentDidMount() {
//        const users = [
//               {
//                    'username': 'root',
//                    'first_name': 'Agata',
//                    'last_name': 'HAHC',
//                    'email': 'izac@yandex.ru'
//               },
//               {
//                    'username': 'no_root',
//                    'first_name': 'Jane',
//                    'last_name': 'Doe',
//                    'email': 'box@yandex.ru'
//               },
//        ]
        axios.get('http://127.0.0.1:8000/api/user/')
        .then(response=> {
            const users = response.data
        this.setState(
            {
                'users': users
                }
            )
      }).catch(error => console.log(error))

}
        render() {
            return(
                <div>
                    <Menu />
                    <UserList users={this.state.users} />
                    <Footer />
                </div>

            )
        }

}

export default App;
