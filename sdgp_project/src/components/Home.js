import React from 'react';
import Welcome from './Welcome';
import AboutWatcher from './AboutWatcher';
 

class Home extends React.Component{
    render(){
        return (
            <div>
                <Welcome/>
                <AboutWatcher/>
            </div>
        );
    };
}
export default Home;