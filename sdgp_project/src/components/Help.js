import React, { Component } from 'react';
import Features from '../components/Features'
import Use from '../components/UseCase'

class Help extends Component {
    
    render() { 
        return ( 
            <div>  
              <header>

              </header>
              <section>
                 <Features/>
                 <Use/>
              </section>
              <footer>

              </footer>
            </div>
         );
    }
}
 
export default Help;