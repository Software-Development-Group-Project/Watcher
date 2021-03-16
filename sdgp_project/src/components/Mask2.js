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
                    <p> <b>Check People </b></p>
                    <p style = {{textAlign: "justify"}}>This web cam can check whether you're wearing mask or not</p>
                     
                     
                </div>
        );
          
          
        
 
    }
}

 
export default Mask;