import SvgColor from 'src/components/svg-color';

// ----------------------------------------------------------------------

const icon = (name) => (
  <SvgColor src={`/assets/icons/navbar/${name}.svg`} sx={{ width: 1, height: 1 }} />
);

const navConfig = [
  {
    title: '首頁',
    path: '/',
    icon: icon('ic_analytics'),
  },
  {
    title: '貓貓聊天室',
    path: '/chat',
    icon: <img src='/assets/icons/chat.png' alt='chat'/>,
  },
  {
    title: '貓貓圖鑑',
    path: '/all-cats',
    icon: icon('ic_user'),
  },
  {
    title: '貓貓推薦',
    path: '/recommend',
    icon: icon('ic_blog'),
  },
  {
    title: '登入',
    path: '/login',
    icon: icon('ic_lock'),
  },
  // {
  //   title: 'Not found',
  //   path: '/404',
  //   icon: icon('ic_disabled'),
  // },
];

export default navConfig;
