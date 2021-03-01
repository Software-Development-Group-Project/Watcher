import React, { Component } from 'react';
import img from '../images/ofi.jpg'

class Office extends Component {
     
    render() { 
        const styles = {
            width: "300px",
            margin: "auto",
            fontSize: "15px"
            
        } 

        return ( 
            <div style = {styles} >
                <h3>Office</h3>
                <img src= { img } width = "300px" height = "250px" alt = "a office" /> 
                <p style = {{textAlign: "justify"}}>The Face Mask Detection System can be used at offices because it will help to identify 
                    employees who are not wear a mask and alert them and also the management. Watcher will 
                    help to ensure the safety of all employees because that is the most important thing in 
                    this situation, and we can use watcher in the entrance also to check them </p>
                 
            </div>    
             
         );
    }
}

export default Office;