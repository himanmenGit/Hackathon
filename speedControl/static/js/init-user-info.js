function initUserInfo() {
  var token = getCookie('token')
  if (token) {
    getUserInfo(token)
  }
}

function getUserInfo(token) {
  axios({
    url: 'http://localhost:8000/api/members/info/',
    method: 'get',
    headers: {
      Authorization: 'Token '.concat(token),
    }
  }).then(function(response) {
    var user = response.data.user
    setUserInfo(user)
  }).catch(function(error) {
    console.log(error.response.data)
  })
}

function setUserInfo(user) {
  $('h1#user-info').text(user.nickname.concat('(으)로 로그인 중입니다.'));
  $('img#user-profile').attr('src', user.img_profile_url);
  $('h1#user-info').removeClass('none');
  $('form#input').addClass('none');
  $('#btn-facebook').addClass('none');
}
