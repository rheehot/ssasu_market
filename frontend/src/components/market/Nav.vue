<template>
  <div class="nav">
    <router-link
      style="text-decoration: none; color: inherit;"
      :to="{ name: 'home', params: { id: home }}"
    >
      <div class="home">
        <img class="homeIcon" src="../../assets/imgs/marketHome.png" alt />홈
      </div>
    </router-link>
    <router-link
      style="text-decoration: none; color: inherit;"
      :to="{name:'mstore', params:{id:home}}"
    >
      <div class="store">
        <img class="storeIcon" src="../../assets/imgs/marketStore.png" alt />상점
      </div>
    </router-link>
    <router-link
      style="text-decoration: none; color: inherit;"
      :to="{name:'community',params:{id:home}}"
    >
      <div class="community">
        <img class="communityIcon" src="../../assets/imgs/marketCommunity.png" alt />게시판
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Nav",
  props: {
    home: { type: Number }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.nav {
  background-color: #fdafd063;
  border-right: 1px solid rgba(143, 141, 141, 0.534);
  font-family: "Jua", sans-serif;
  color: #2e0202;
  text-align: center;
}

.home {
  height: 33.3vh;
  /* line-height: 33.3vh; */
  border-bottom: 1px solid rgba(143, 141, 141, 0.534);
  font-size: 1.4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.home:hover {
  background-color: #ff006a2f;
}
.homeIcon {
  width: 140px;
}
.store {
  height: 33.3vh;
  /* line-height: 33.3vh; */
  border-bottom: 1px solid rgba(143, 141, 141, 0.534);
  font-size: 1.4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.store:hover {
  background-color: #ff006a2f;
}
.storeIcon {
  width: 140px;
}
.community {
  height: 33.3vh;
  /* line-height: 33.3vh; */
  border-bottom: 1px solid rgba(143, 141, 141, 0.534);
  font-size: 1.4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.community:hover {
  background-color: #ff006a2f;
}
.communityIcon {
  width: 120px;
}
</style>
