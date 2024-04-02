import { css } from '@emotion/react';

export const teamMembersStyles = css`
.team-members {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
`;

export const teamMemberStyles = css`
.team-member{
  flex: 0 0 calc(33.33% - 20px);
  padding: 20px;
  margin: 10px;
  text-align: center;

  img {
    border-radius: 50%;
    margin-bottom: 20px;
  }

  h3 {
    margin-bottom: 10px;
    display: inline-block;
  }
}
`;
