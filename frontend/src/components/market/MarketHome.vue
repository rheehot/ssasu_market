<template>
  <div class="home">
    <div id="MarketDetail">
      <MarketInfo
        :name="data.name"
        :score="data.avg_score"
        :star="data.star"
        :reviewNum="data.reviewNum"
        :address="data.address"
        :time="data.time"
        :tell="data.phone"
      />
      <MarketVisit></MarketVisit>
    </div>
  </div>
</template>

<script>
import MarketInfo from "./MarketInfo.vue";
import MarketVisit from "./MarketVisit.vue";
import axios from "axios";

export default {
  mounted() {
    console.log(this.params);
    this.$emit("marketNum", this.params.id);
    axios
      .get("http://127.0.0.1:8000/market/get_market/" + this.params.id + "/")
      .then(response => {
        this.data = response.data;
      });
  },
  computed: {
    params: function() {
      return this.$route.params;
    }
  },
  name: "MarketHome",
  data() {
    return {
      data: {
        name: "광장시장",
        score: 5.0,
        star: "★★★★★",
        reviewNum: 3,
        address: "서울 종로구 창경궁로 88",
        time: "매일 09:00 ~ 18:00",
        tell: "02-2267-0291"
      }
    };
  },
  components: {
    MarketInfo,
    MarketVisit
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  margin: 3rem 3rem;
}
#MarketDetail {
  position: absolute;
  overflow: auto;
  top: 0;
  width: 70%;
  height: 80%;
}
#MarketDetail::-webkit-scrollbar {
  width: 10px;
}
#MarketDetail::-webkit-scrollbar-thumb {
  background-color: #88093e;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
#MarketDetail::-webkit-scrollbar-track {
  background-color: rgba(221, 149, 149, 0.726);
  border-radius: 10px;
  box-shadow: inset 0px 0px 5px white;
}
</style>