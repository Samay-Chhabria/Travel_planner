export default function PageContainer({ children, className = '', as: Component = 'div' }) {
  return (
    <Component
      className={['mx-auto w-full max-w-content px-4 sm:px-6 lg:px-8', className]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </Component>
  );
}
