import Vue from 'vue'
import Router from 'vue-router'
import dbInfo from '@/components/dbInfo'
import tableInfo from '@/components/tableInfo'
import index from '@/components/index'

Vue.use(Router)

export default new Router({
  routes: [{
      path: '/dbInfo',
      name: 'dbInfo',
      component: dbInfo
    },
    {
      path: '/tableInfo',
      name: 'tableInfo',
      component: tableInfo
    },
    {
      path: '/index',
      name: 'index',
      component: index
    },
  ]
})
