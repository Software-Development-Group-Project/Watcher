import React, { Component } from 'react';
import University from './university';
import Office from './Office'
import '../CSS/UseCase.css'

class UseCase extends Component {
    
    render() {
        
        const styles = {
            marginBottom : 30,
            marginTop : 20
        } 
        return ( 
            <div className="container" id="play">
                <div class="row">
                    <div class="col-sm"><h1 style = {styles} > Use Case </h1></div>     
                </div>
                <div class="row">
                    <div class="col-sm"><University /></div>
                    <div class="col-sm"><Office /></div>
                </div>
            </div>

         );
    }
}
 
export default UseCase;