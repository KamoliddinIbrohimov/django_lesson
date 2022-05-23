import React,{ Component } from 'react'
import axios from 'axios';
// const list = [
//     {"id":1,"title":"Bugun django darslarini ko'rishim kerak","body":"bugun judayam muhum kun"},
//     {"id":2,"title":"bugun kitobni 200-betigacha o'qib chiqishim kerak","body":"bu kitob  menga judayam yoqadi"},
//     {"id":3,"title":"django rest frinvokni o'rganishim kerak","body":"buni qilishim kerak"}
// ]

// class App extends Component{
//     constructor(props){
//         super(props);
//         this.state={list}
//     }
//     render(){
//         return(
//             <div>
//                 {this.state.list.map(item=>(
//                     <div key={item.id}>
//                     <h1>{item.title}</h1>
//                     <p>{item.body}</p>
//                     </div>
//                 ))}
//             </div>
//         )
//     }
// }
// export default App

class App extends Component{
    state = {
        todos:[]
    };
    //yangi
    componentDidMount(){
        this.getTodos();
    }

    getTodos(){
        axios
        .get('http://127.0.0.1:8000/api/')
        .then(res=>{
            this.setState({todos:res.data});
        })
        .catch(err=>{
            console.log(err)
        })
    }
    render(){
        return(
            <div>
                {this.state.todos.map(item=>(
                    <div key={item.id}>
                        <h1> {item.title}</h1>
                        <span>{item.body}</span>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;