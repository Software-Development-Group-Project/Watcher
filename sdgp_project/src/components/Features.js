import React, { Component } from 'react';
import Alert from '../components/Alert';
import Mask from '../components/Mask2';
import Person from '../components/Person';
import '../CSS/Features.css'

class Features extends Component {
     
    render() { 
        return ( 
            <div className="container" id="feature">
                <div class="row">
                    <div class="col-sm"><h1 id="heading"> Features of Watcher </h1></div>     
                </div>
                <div class="row">
                    <div class="col-sm"><Mask /></div>
                    <div class="col-sm"><Alert /></div>
                    <div class="col-sm"><Person /></div>
                </div>
            </div>
         );
    }
}
 
export default Features;