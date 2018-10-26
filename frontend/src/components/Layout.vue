<template>
  <el-container>
    <el-aside width="" v-show="$auth.check()">
      <el-menu :router="true" class="el-menu-vertical" :collapse="navMenuCollapsed">
        <el-menu-item index="/">
          <i class="el-icon-menu"></i>
          <span slot="title">Dashboard</span>
        </el-menu-item>
        <el-menu-item index="/purchases">
          <i class="el-icon-tickets"></i>
          <span slot="title">Purchases</span>
        </el-menu-item>
        <el-menu-item index="/sales">
          <i class="el-icon-tickets"></i>
          <span slot="title">Sales</span>
        </el-menu-item>
        <el-menu-item index="/reset-password">
          <i class="el-icon-setting"></i>
          <span slot="title">Profile</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header v-show="$auth.check()">
        <el-row :gutter="10">
          <el-col :md="4">
            <el-switch v-model="navMenuCollapsed"></el-switch>
          </el-col>
          <el-col class="hidden-sm-and-down" :md="12">
            <el-breadcrumb separator-class="el-icon-arrow-right">
              <el-breadcrumb-item :to="{ path: '/' }">Retail Management</el-breadcrumb-item>
            </el-breadcrumb>
          </el-col>
          <el-col :sm="24" :md="8" style="text-align: right">
            <el-dropdown @command="handleCommand">
              <i class="el-icon-setting" style="margin-right: 15px"></i>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="logout">Logout</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
            <span>{{ $auth.user().username }}</span>
          </el-col>
        </el-row>
      </el-header>
      <el-main id="main-layout">
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      navMenuCollapsed: true
    }
  },
  methods: {
    logout () {
      this.$log('logout')
      this.$auth.logout({
        redirect: 'login',
        makeRequest: false
      })
    },
    handleCommand (command) {
      this[command]()
    }
  },
  watch: {
    navMenuCollapsed: function (val) {
      localStorage.setItem('layoutNavMenuCollapsed', val ? 'true' : 'false')
    }
  },
  beforeMount: function () {
    this.navMenuCollapsed = localStorage.getItem('layoutNavMenuCollapsed') === 'true'
  },
  mounted: function () {
    if (this.$auth.check()) {
      // load current user data
    }
  }
}
</script>

<style scoped>
.el-menu-vertical:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

</style>
