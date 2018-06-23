import React ,{Component} from 'react';
import './header.css'

// const HeaderProp = (prop) => (
//     <div >
//         <h1>{prop.title}</h1>
//         <div>
//             {
//                 prop.username?
//                 (<div>
//                     <p>{prop.username}</p>
//                     <input type="button" value="settings"/>
//                 </div>):
//                 (<div>
//                     <input type="button" value="Login"/>
//                     <input type="button" value="Signup"/>
//                 </div>)
//             }

//         </div>
//     </div>
// )
class HeaderProp extends Component{
    constructor(props){
        super(props)
        this.state ={
            title : props.title,
            user : props.username,
            isLoggedin : props.username ? true : false,
        }
    }
    toggleUser =()  =>{
        this.setState(prev=>({isLoggedin:!prev.isLoggedin}));
    }
    render(){
        return(
            <div className="headerComp">
                <h1>{this.state.title}</h1>
                <div className="menu" onClick={this.toggleUser}>
                    {
                        this.state.isLoggedin?<button>Login</button>:<button>Logout</button>
                    }
                </div>
            </div>
        );
    }
}
export default HeaderProp;