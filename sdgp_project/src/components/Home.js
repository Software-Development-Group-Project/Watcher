import React from 'react';
import Welcome from './Welcome';
import About from './AboutS';
 

class Home extends React.Component{
    render(){
        return (
            <div>
                <Welcome/>
                <About/>
            </div>
        );
    };
}
export default Home;