import React from 'react';

const UserItem = ({user}) => {
        return (
            <div class="row">
                    <div class="col-md">
                    <h2>
                        {user.username}
                    </h2>
                    </div>

                    <div class="col-md">
                    <h2>
                            {user.first_name} {user.last_name}
                    </h2>
                    </div >

                    <div class="col-md">
                    <h2>
                            {user.email}
                    </h2>
                    </div>
            </div>
        )

}

const UserList = ({users}) => {

        return(
            <div class="container">
                <div class="row">
                    <div class="col-md"> <h1> Login </h1> </div>
                    <div class="col-md"> <h1> Name </h1> </div>
                    <div class="col-md"> <h1> Email </h1> </div>
                </div>
                {users.map((user) => (<UserItem user={user} />))}
            </div>

        )

}

export default UserList
