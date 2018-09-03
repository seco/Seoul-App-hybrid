/*********************************

*********************************/
import Vue from 'vue';
import Router from 'vue-router';

import Home from '../components/Home';
import Services from '../components/services';

Vue.use(Router);

export default new Router({
  mode: 'history',
    routes: [
        {
          path: '/',
          component: Services
        },
        {
          path: '/services',
          component: Services
        }
    ]
});
