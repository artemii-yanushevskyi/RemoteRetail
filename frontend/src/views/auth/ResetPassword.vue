<template>
<el-row type="flex" class="row-bg" justify="center" align="middle" style="margin-top: 4rem">
  <el-col :xs="16" :sm="12" :md="8" :lg="6" :xl="6">
    <el-form :model="form" ref="form" :rules="validationRules" label-position="top">
      <el-form-item label="Old password" prop="old_password">
        <el-input v-model="form.old_password" type="password" auto-complete="off" @keyup.enter="submitForm('form')"></el-input>
      </el-form-item>
      <el-form-item label="New password" prop="new_password1">
        <el-input v-model="form.new_password1" type="password" auto-complete="off" @keyup.enter="submitForm('form')"></el-input>
      </el-form-item>
      <el-form-item label="Repeat new password" prop="new_password2">
        <el-input v-model="form.new_password2" type="password" auto-complete="off" @keyup.enter="submitForm('form')"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button  :disabled="submitButtonDisabled" type="primary" @click="submitForm('form')">Change password</el-button>
      </el-form-item>
    </el-form>
  </el-col>
</el-row>
</template>


<script>
import apiClient from '../../api'

export default {
  data () {
    let self = this
    let validatePasswordEquality = (rule, value, callback) => {
      if (self.form.new_password1 !== value) {
        callback(new Error('Enter equal passwords.'))
      }
      callback()
    }
    return {
      submitButtonDisabled: false,
      form: {
        old_password: '',
        new_password1: '',
        new_password2: ''
      },
      validationRules: {
        old_password: [
            { required: true, message: 'Please enter your old password', trigger: 'blur' }
        ],
        new_password1: [
            { required: true, message: 'Please enter your new password', trigger: 'blur' }
        ],
        new_password2: [
            { required: true, message: 'Please repeat your new password', trigger: 'blur' },
            { validator: validatePasswordEquality, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    cleanForm () {
      this.form.old_password = ''
      this.form.new_password1 = ''
      this.form.new_password2 = ''
    },
    submitForm (formName) {
      let self = this
      this.$refs[formName].validate((valid) => {
        if (!valid) {
          this.$message({
            message: 'Correct your input.',
            showClose: true
          })
        } else {
          self.submitButtonDisabled = true
          apiClient.resetPassword(self.form.old_password,
                                  self.form.new_password1)
            .then((response) => {
              this.$notify({
                title: 'Success',
                type: 'success',
                message: response.data.message
              })
              self.cleanForm()
              self.submitButtonDisabled = false
              self.$router.push('/')
            })
            .catch(() => {
              this.$notify({
                title: 'Error',
                type: 'error',
                message: 'Failed to reset password.'
              })
              self.cleanForm()
              self.submitButtonDisabled = false
            })
        }
      })
    }
  }
}
</script>
