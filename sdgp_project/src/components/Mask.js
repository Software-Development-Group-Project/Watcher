import React, { Component } from 'react';
import img from '../images/mask.png';

class Mask extends Component {
    render() { 
        const styles = {
                width: "300px",
                margin: "auto",
                fontSize: "15px",
                 
            } 
    
        return ( 
                <div style = {styles}>
                    <img src = {img} alt="alert"/> 
                    <p><b> Check people </b></p>
                    <p style = {{textAlign: "justify"}}>the system can check people, they are wearing mask or not</p>
                </div>
        );
 
    }
}
 
export default Mask;