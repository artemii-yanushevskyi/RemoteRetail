<template>
<div id="dashboard" v-if="showDashboard" class="col-btm-20">
  Dashboard
</div>
</template>

<script>
export default {
  data: function () {
    return {
      statisticsLoading: true,
      showDashboard: true
    }
  },
  components: {},
  computed: {},
  methods: {},
  mounted: function () {}
}
</script>

<style lang="scss">
.dashboard-controls {
  padding: 0 20px 10px 20px;
}
</style>
