/*********************************

*********************************/
import Vue from 'vue';
import Router from 'vue-router';

import Home from '../components/Home';
import Servicies from '../components/Servicies';

Vue.use(Router);

export default new Router({
  mode: 'history',
    routes: [
        {
          path: '/',
          name: 'Home',
          component: Home
        },
        {
          path: '/services',
          name: 'Services',
          component: Servicies
        }
    ]
});
