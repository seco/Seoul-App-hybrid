<template>
    <v-app>
        <v-toolbar app color="#598bf9">
            <v-layout row wrap>
                <v-flex xs6 style="text-align:left;">
                    <router-link to="/" style="text-decoration: none;">
                        <v-btn icon flat>
                            <v-icon large color="white">arrow_back</v-icon>
                        </v-btn>
                    </router-link>
                </v-flex>
                <v-flex xs6 style="text-align:right; padding-top: 8px; padding-right: 10px;">
                    <h1 style="color: white;">{{ computedCategoryName }}</h1>
                </v-flex>
            </v-layout>
        </v-toolbar>
        <v-content>
            <v-container style="background-color: #fff;">
                <v-layout wrap align-center>
                    <v-flex xs12>
                        <v-select
                             :items="places"
                             label="- 지역명 -"
                             color="#598bf9"
                             background-color="#aaa"
                             outline
                             v-model="AREANM"
                             autocomplete
                        ></v-select>
                    </v-flex>
                    <v-flex xs12 style="margin-top: -20px;">
                        <v-select
                            :items="places"
                            label="- 소분류 -"
                            color="#598bf9"
                            background-color="#aaa"
                            outline
                            v-model="MINCLASSNM"
                            autocomplete
                        ></v-select>
                    </v-flex>
                    <v-flex xs12 style="margin-top: -20px;">
                        <v-btn
                            block
                            outline
                            large
                            color="#598bf9"
                            @click="getSearchedData"
                        >
                            검색하기
                        </v-btn>
                    </v-flex>
                </v-layout>
            </v-container>
            <v-divider></v-divider>
            <v-container fluid style="padding: 0;">
                <v-layout align-center>
                    <v-flex xs12>
                        <v-list two-line subheader>
                            <v-subheader>
                            </v-subheader>

                            <v-list-tile v-for="item in ServicesData" :key="item.SVCID">
                                <v-list-tile-content>
                                    <v-list-tile-title>{{ item['SVCNM'] }}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{ item['PLACENM'] }}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ServiceList",
        data () {

            return {
                places: [
                    '강남구',
                    '강동구',
                    '강북구',
                    '강서구',
                    '관악구',
                    '광진구',
                    '구로구',
                    '노원구',
                    '도봉구',
                    '동대문구',
                    '동작구',
                    '마포구',
                    '서대문구',
                    '서초구',
                    '성동구',
                    '성북구',
                    '송파구',
                    '양천구',
                    '영등포구',
                    '용산구',
                    '은평구',
                    '종로구',
                    '중구',
                    '중랑구'
                ],
                ServicesData: [],
                MAXCLASSNM: '',
                MINCLASSNM: '안뇽',
                AREANM: '안뇽'
            }
        },
        created: function() {
            this.MAXCLASSNM = this.$store.state.category;

            let jArray = new Array();
            axios.post('/services', {MAXCLASSNM: this.$store.state.category})
                .then(function (response) {

                    for (var idx in response.data) {
                        jArray.push( response.data[idx] );
                    }

                })
                .catch(function (error) {
                    console.log(error);

                    return [];
                });

            this.ServicesData = jArray;

            console.log(this.ServicesData);
        },
        computed: {
            computedCategoryName() {
                let cate = this.$store.state.category;
                let result = '';

                if (cate === '교육') {
                    result = '교육신청';
                } else if (cate === '진료') {
                    result = '진료예약';
                }else {
                    result = cate;
                }

                return result;
            }
        },
        methods: {
            getSearchedData : (event) => {
                console.log(this.AREANM);
                console.log(this.MINCLASSNM);
            }
        }
    }
</script>

<style scoped>

</style>