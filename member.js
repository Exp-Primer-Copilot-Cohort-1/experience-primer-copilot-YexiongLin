function skillsMember() {
  return {
    restrict: 'E',
    scope: {
      member: '=',
      title: '@'
    },
    templateUrl: 'components/member.html'
  };
}
