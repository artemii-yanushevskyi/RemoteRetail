<template>
<el-row type="flex" class="row-bg" justify="center" align="middle" style="margin-top: 4rem">
  <el-col :xs="16" :sm="12" :md="8" :lg="6" :xl="6">
    <el-form :model="form" ref="form" :rules="validationRules" label-position="top">
      <el-form-item label="Username" prop="username">
        <el-input v-model="form.username" type="text" auto-complete="off" @keyup.enter="submitForm('form')"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input v-model="form.password" type="password" auto-complete="off" @keyup.enter="submitForm('form')"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('form')">Submit</el-button>
      </el-form-item>
    </el-form>
  </el-col>
</el-row>
</template>

<script>
export default {
  data () {
    return {
      form: {
        username: '',
        password: ''
      },
      validationRules: {
        username: [
            { required: true, message: 'Please enter your username', trigger: 'blur' }
        ],
        password: [
            { required: true, message: 'Please enter your password', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      let self = this
      this.$refs[formName].validate((valid) => {
        if (!valid) {
          this.$message({
            message: 'Enter valid credentials.',
            showClose: true
          })
        } else {
          let redirect = this.$auth.redirect()
          this.$auth.login({
            headers: {
              'Content-Type': 'application/json'
            },
            data: this.form,
            rememberMe: false,
            redirect: {name: redirect ? redirect.from.name : 'dashboard'},
            success (res) {
              self.$log(res)
            },
            error (err) {
              self.$message({
                message: 'Failed to login.',
                type: 'error',
                showClose: true
              })
              self.$log(err)
            }
          })
        }
      })
    }
  }
}
</script>

